# Project DestinyFileIO
## Installation
Travis CI Status:  [![BuildStatus](https://travis-ci.org/msanchez5/DestinyFileIO.svg?branch=master)](https://travis-ci.org/msanchez5/DestinyFileIO)

Project DestinyFileIO is a small file extracting information.

## Getting Started
Make sure you clone the DestinyFileIO repo:
```
$ git clone https://github.com/msanchez5/DestinyFileIO.git

```
After cloning the repo, here are some commands you need to do to run the tester.
```
$ cd DestinyFileIO/example
$ run python test.py
```

## Contribution
Feel free to contribute into this project and keep looking at the issues list.

Have an idea? Found a bug? See [Contribution page](docs/CONTRIBUTIN.md).

## Documentation
The following table are collection of functionality that needs to be implemented.

| Function Name | Description | Input | Expected Output
| ----- | ----- | ----- | ----- |
| `getFilePathName(path)` | Filename with out the path | `/home/marvins/mydata.txt` | `mydata.txt` |
| `getFileSize(path)` | File size in bytes | `/home/marvins/mydata.txt` | 129 Kb |
| `convertSHA(path)` | SHA1 digest for a file at the given path | The quick brown fox jumps over the lazy dog | 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 |
| `convertMD5(path)` | MD5 digest for a file at the given path | The quick brown fox jumps over the lazy dog | 9e107d9d372bb6826bd81d3542a419d |

#### Params

- **String** `path`: The path to the file you want.

## License
[MIT](docs/LICENSE.md) © [Marvin Sanchez](http://marvinrsanchez.wordpress.com/)
