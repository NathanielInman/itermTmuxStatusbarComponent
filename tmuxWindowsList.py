import asyncio
import iterm2

async def main(connection):
    component = iterm2.StatusBarComponent(
        short_description='Tmux Windows List',
        detailed_description='Get list of windows from running tmux session',
        exemplar='¹ WindowName',
        update_cadence=1,
        identifier='github.nathanielinman.iterm-components.tmuxwindows',
        knobs=[],
    )
    def pretty(string,activeWindow):
        collection = string.split('|')
        for index, item in enumerate(collection):
            if item == activeWindow:
                collection[index] = '«'+item+'»'
            elif index % 2 is 0:
                collection[index] = item.replace('0','⁰').replace('1','¹').replace('2','²').replace('3','³').replace('4','⁴').replace('5','⁵').replace('6','⁶').replace('7','⁷').replace('8','⁸').replace('9','⁹')
        return ''.join(collection)

    @iterm2.StatusBarRPC
    async def tmux_windows_list(knobs):
        nl = '\n'
        proc = await asyncio.create_subprocess_shell(
            'tmux display-message -p \'#I\'',
            stdout=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        activeWindow = stdout.decode().strip()
        proc = await asyncio.create_subprocess_shell(
            'tmux list-windows -F \'#I| #W |\'',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await proc.communicate()
        cleanedString = stdout.decode().strip().replace(nl,'')
        if stderr:
            return 'tmux not running'
        else:
            return f'{pretty(cleanedString,activeWindow)}'

    await component.async_register(connection, tmux_windows_list)

iterm2.run_forever(main)
