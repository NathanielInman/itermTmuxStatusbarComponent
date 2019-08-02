import asyncio
import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Tmux Session Name',
        detailed_description='Get session name from running tmux session',
        exemplar='Tmux Session Name',
        update_cadence=2,
        identifier='github.nathanielinman.iterm-components.tmuxsessionname',
        knobs=[],
    )

    @iterm2.StatusBarRPC
    async def tmux_session_name(knobs):
        proc = await asyncio.create_subprocess_shell(
            'tmux display-message -p \'#S\'',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        return f'{stdout.decode().strip()}' if not stderr else 'tmux not running!'

    await component.async_register(connection, tmux_session_name)

iterm2.run_forever(main)
