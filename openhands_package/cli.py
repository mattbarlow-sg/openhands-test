"""Tests the openhands-ai package."""
import asyncio
import os

from openhands.controller.state.state import State
from openhands.core.config import AppConfig, SandboxConfig
from openhands.core.main import run_controller
from openhands.runtime import get_runtime_cls

TEST_RUNTIME = "eventstream"

_ = get_runtime_cls(TEST_RUNTIME)

cwd = os.getcwd()

CONFIG = AppConfig(
    max_iterations=15,
    max_budget_per_task=15,
    default_agent='CodeActAgent',
    debug=True,
    runtime=TEST_RUNTIME,
    workspace_base=cwd,
    workspace_mount_path=cwd,
    sandbox=SandboxConfig(
        use_host_network=True,
    ),
)


def main():
    """Run a simple test."""
    task = "Write a shell script 'hello.sh' that prints 'hello'. "\
        "Do not ask me for confirmation at any point."

    final_state: State | None = asyncio.run(
        run_controller(CONFIG, task, exit_on_message=True)
    )
    print(final_state)


if __name__ == '__main__':
    main()
