# Add an auditing hook
sys.addaudithook(hook: Callable[str, tuple]) -> None

# Raise an event with all auditing hooks
sys.audit(str, *args) -> None
