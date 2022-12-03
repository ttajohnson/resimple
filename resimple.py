import os
import wave
import pyaudio

# ReSimple v.0.1.2, Rel 12/3/2022
# Author: Timothy Tyson Alan Johnson (@ttajohnson on GitHub)
# Included is a directory with some basic subdirs of .wav samples to test with.
# Filepath Example - C:\Users\You\Desktop\resimple\samples


class ReSimple:
    def __init__(self):
        self.filepath = input(
            "Enter path to Sample Directory: "
        )  # Set a filepath to a directory that contains audio samples...
        os.chdir(self.filepath)  # and change your CWD to that directory.

    def display_current(self):
        cwd = os.getcwd()  # Grab the CWD...
        print("Current Working Directory:\n\t" + cwd)  # and display it to the user.

    def display_content(self):
        contents = os.listdir()  # Initiate a list of directory contents.
        total = len(contents)  # Count and hold the total number of contents.
        contents.insert(0, "Contents:")  # Really just for formatting purposes.
        if (
            total > 10
        ):  # Some contents may exceed hundreds, if there are less than 10 we'll go ahead and display them.
            choice = input(
                f"{total} contents found:\n\t1. Preview Contents\n\t2. View All Contents\n"
            )
            if choice == "1":
                limit = 10
                preview = len(contents)
                for i in range(0, preview - limit):
                    contents.pop()
                print(*contents, sep="\t\n\t")
                print("\n")
            elif choice == "2":
                print(*contents, sep="\t\n\t")
            else:
                print("Invalid Choice!")
        else:
            print(*contents, sep="\t\n\t")
            print("\n")

    def change_cwd(self):
        switch = input("\nEnter directory name or '..' to go back: ")

        if switch in os.listdir():
            new_directory = os.getcwd() + "\\" + switch
            os.chdir(new_directory)
            self.display_current()
        elif switch == "..":
            os.chdir(switch)
            self.display_current()
        else:
            print("Invalid Choice!")

    def play_wav(self, wavfile):
        CHUNK = 1024
        wf = wave.open(wavfile, "rb")
        pa = pyaudio.PyAudio()

        stream = pa.open(
            format=pa.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True,
        )

        data = wf.readframes(CHUNK)

        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close
        pa.terminate

    def play_files(self):
        cwd = os.getcwd()
        wavfiles = os.listdir()
        for wavfile in wavfiles:
            suffix = ".wav"  # Analysis files are often created by Ableton after being used in a project...
            if wavfile.endswith(
                suffix
            ):  # These two lines ensure that we skip over any .asd or other file types that cannot be played.
                while True:
                    print(wavfile)
                    self.play_wav(cwd + "/" + wavfile)
                    repextop = input(
                        "\n1. Play Again\n2. Preview Next File\n3. End File Previews\n"
                    )
                    if repextop == "1":
                        continue
                    elif repextop == "2":
                        break
                    elif repextop == "3":
                        return False
            else:
                continue

    def rename_files(self):
        i = 0
        wavfiles = os.listdir()
        batch_name = input("Enter batch name for files: ").title()
        for file in wavfiles:
            suffix = ".wav"
            if file.endswith(suffix):
                new_name = batch_name + "(" + str(i) + ")" + ".wav"
                if new_name == file:
                    break
                else:
                    os.rename(file, new_name)
                i += 1
            else:
                continue
        print(f"Files renamed to {batch_name}().wav")


def main():

    print("\t-Welcome to ReSimple-")

    options = [
        "Options:",
        "1. Display CWD",
        "2. Display Contents",
        "3. Change CWD",
        "4. Play Files",
        "5. Rename Files",
        "6. End ReSimple",
    ]

    resimple = ReSimple()

    while True:
        print(*options, sep="\t\n\t")

        choice = input()

        if choice == "1":
            resimple.display_current()
        elif choice == "2":
            resimple.display_content()
        elif choice == "3":
            resimple.change_cwd()
        elif choice == "4":
            try:
                resimple.play_files()
            except:
                print("No .wav files detected.")
        elif choice == "5":
            resimple.rename_files()
        elif choice == "6":
            print("Thanks for using ReSimple!")
            return False
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()
