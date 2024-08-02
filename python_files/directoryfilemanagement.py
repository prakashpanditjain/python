import os


if __name__ == '__main__':
    # print("This is the current working directory \n",os.getcwd())

    # get the current working directory
    cwd = os.getcwd()
    cwd = str(os.listdir(cwd)[0])
    print(cwd)

    # Rename the directory
    rename = os.listdir()
    # print("".join(i for i in (rename[0].split("_"))))
    rename = "".join(i for i in (rename[0].split("_")))

    # renaming the directory
    # os.rename(cwd,rename)


    # get the execution path
    exec_path = os.get_exec_path()
    # print("\n".join(i for i in exec_path))