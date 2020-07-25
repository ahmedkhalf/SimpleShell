from subprocess import check_call, CalledProcessError
import readline

while True:
    try:
        command = input("$ ")
    except EOFError:
        break
    except KeyboardInterrupt:
        print()
        continue

    if command.strip() == "exit":
        break
    else:
        try:
            check_call(command, shell=True)
        except CalledProcessError as e:
            pass