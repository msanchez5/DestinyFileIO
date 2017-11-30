# Project DestinyFileIO
Travis CI Status:  [![BuildStatus](https://travis-ci.org/msanchez5/DestinyFileIO.svg?branch=master)](https://travis-ci.org/msanchez5/DestinyFileIO)

Project DestinyFileIO is a small file extracting information.

## Getting Started

To get a local copy of the current code, clone it using git:
```
$ git clone git@github.com:msanchez5/DestinyFileIO.git
$ cd DestinyFileIO/Python
$ run python DestinyFileIO.py
```

## Contributing
Feel free to contribute into this project and keep looking at the issues list.
Special thank you for the following contributors:

| Name | Github Account |
| ------ | ------ |
| Marvin S | [msanchez5](https://github.com/msanchez5) |
| Fateh S | [Fatehsandhu](https://github.com/Fatehsandhu) |

## Functionality
The following table are collection of functionality that must needs implementation.

| Function Name | Description | Input | Expected Output
| ----- | ----- | ----- | ----- |
| getFilePathName(path) | Filename with out the path | /home/marvins/mydata.txt | mydata.txt |
| getFileSize(path) | File size in bytes | /home/marvins/mydata.txt | 129 Kb |
| convertSHA(path) | SHA1 digest for a file at the given path | The quick brown fox jumps over the lazy dog | 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 |
| convertMD5(path) | MD5 digest for a file at the given path | The quick brown fox jumps over the lazy dog | 9e107d9d372bb6826bd81d3542a419d |

## License
MIT
