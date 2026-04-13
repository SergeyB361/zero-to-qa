from dataclasses import dataclass


TRANSITIONS = {
    "draft": {"submit": "in_review", "cancel": "cancelled"},
    "in_review": {"approve": "approved", "reject": "draft", "cancel": "cancelled"},
    "approved": {"archive": "archived"},
    "cancelled": {},
    "archived": {},
}

TERMINAL_STATES = {"cancelled", "archived"}
ALL_EVENTS = {"submit", "approve", "reject", "cancel", "archive"}


@dataclass(frozen=True)
class TransitionCase:
    start_state: str
    event: str
    expected_state: str | None
    allowed: bool


class WorkflowMachine:
    def __init__(self, state: str) -> None:
        self.state = state

    def allowed_events(self) -> set[str]:
        return set(TRANSITIONS.get(self.state, {}))

    def can_apply(self, event: str) -> bool:
        return event in self.allowed_events()

    def apply(self, event: str) -> str:
        if not self.can_apply(event):
            raise ValueError(f"forbidden transition: {self.state} --{event}--> ?")
        self.state = TRANSITIONS[self.state][event]
        return self.state


def generate_transition_cases() -> list[TransitionCase]:
    cases: list[TransitionCase] = []
    for state, mapping in TRANSITIONS.items():
        for event in sorted(ALL_EVENTS):
            allowed = event in mapping
            cases.append(
                TransitionCase(
                    start_state=state,
                    event=event,
                    expected_state=mapping.get(event),
                    allowed=allowed,
                )
            )
    return cases


if __name__ == "__main__":
    machine = WorkflowMachine("draft")
    print("=== happy path ===")
    print("start:", machine.state)
    print("after submit:", machine.apply("submit"))
    print("after approve:", machine.apply("approve"))
    print("after archive:", machine.apply("archive"))
    print("terminal:", machine.state in TERMINAL_STATES)
    print()

    print("=== forbidden transition ===")
    try:
        WorkflowMachine("draft").apply("approve")
    except ValueError as error:
        print(error)
    print()

    print("=== model-driven test cases ===")
    cases = generate_transition_cases()
    allowed_cases = [case for case in cases if case.allowed]
    forbidden_cases = [case for case in cases if not case.allowed]
    print("allowed cases:", len(allowed_cases))
    print("forbidden cases:", len(forbidden_cases))
    print("sample allowed:", allowed_cases[:3])
    print("sample forbidden:", forbidden_cases[:3])