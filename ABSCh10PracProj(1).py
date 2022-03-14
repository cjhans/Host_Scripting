import os, shutil

def selectiveCopy(inputFolder, ext, outputFolder):
    """Args:
        inputFolder (str): Path of folder to search in
        ext (str): file extension to search for
        outputFolder (str): Path of folder to copy files into
    Returns:
        None
    """

    resultFolder = os.path.abspath(outputFolder)

    for folderName, subFolder, filename in os.walk(inputFolder):
        for file in filename:
            if file.endswith(ext):
                filepath = os.path.join(os.path.abspath(folderName), file)
                if not os.path.exists(resultFolder):
                    os.makedirs(resultFolder)
                if os.path.dirname(filepath) != resultFolder:
                    shutil.copy(filepath, resultFolder)
                    print(f'Copied {filepath} to result folder')

selectiveCopy('.', 'png', 'result')