# itermTmuxStatusbarComponent
A set of tmux statusbar components that shows active windows, inactive or session name

![Statusbar example shows inactive and active tmux windows](/screenshots/example.png)

![Statusbar example shows current tmux session name](/screenshots/example2.png)
## Components

### Tmux Session Name
Shows the current session name for the active tmux session.

### Tmux Window List
Shows the current windows for the active tmux session and indicates which window is currently active.

## Installation

At the moment, I don't know a better way to do this.
If you know one, I would happily review a pull request!

### Auto-loading the components

iTerm2 expects the custom status bar components that act as long-running processes to be in its `AutoLaunch` folder:

```shell
$ git clone git@github.com:daneah/iterm-components.git
$ cd ${HOME}/Library/Application\ Support/iTerm2/Scripts
$ mkdir -p AutoLaunch && cd AutoLaunch
$ ln -s /path/to/iterm-components/some_component.py .  # For each component you want to install; cp them if preferred
```

With iTerm2 running and selected go to **Scripts > AutoLaunch** and select the scripts you linked or copied into the AutoLaunch folder. You may be prompted to download the Python runtime.

### Configuring the components

After the components you want are present in the `AutoLaunch` folder and selected in the **Scripts > AutoLaunch** menu, iTerm2 should make them available to use.

Read [the instructions for using status bar components](https://www.iterm2.com/3.3/documentation-status-bar.html) and drag them where you like.

## Thanks
Special thanks to @daneah for his excellent iterm2 component examples available [here](https://github.com/daneah/iterm-components).

And of course none of this wouldn't be possible without @gnachman's [iterm2](https://github.com/gnachman/iTerm2)!
