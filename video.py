from subprocess import call


def video(e):
    name = e.get()
    print('Downloading {} video'.format(name))

    search = ["ytsearch:" + name]
    command = ['youtube-dl', '-o', '/home/umang/Videos/%(title)s.%(ext)s+']
    command.extend(search)
    call(command, shell=False)
    print()