# Project DestinyFileIO

## Installation

Travis CI Status:  [![BuildStatus](https://travis-ci.org/msanchez5/DestinyFileIO.svg?branch=master)](https://travis-ci.org/msanchez5/DestinyFileIO)

Project DestinyFileIO is a small file extracting information.

## TABLE OF CONTENT

* [Contribution page](docs/CONTRIBUTING.md).
* [Code of Conduct page](docs/CODE-OF-CONDUCT.md)
* [Destiny File IO](example/DestinyFileIO.py)
* [Tester](example/test.py)

## Getting Started

Make sure you clone the DestinyFileIO repo:

```bash
$git clone https://github.com/msanchez5/DestinyFileIO.git
```

After cloning the repo, execute the following commands to run the tester.

```bash
$cd DestinyFileIO/example
$run python test.py
```

## Contribution

Feel free to contribute to this project and keep looking at the issues list.

Have an idea? Found a bug? See [Contribution page](docs/CONTRIBUTING.md).

| Label Name | Description |
| ----- | ----- |
| `good first issue` | Less complex issues which would be good first issues to work on |
| `questions` | Questions rather than bugs (ie. What should I do?)|
| `help-wanted` | Your help would be appreciated |
| `on-going` | It is being worked on right now |
| `assigned` | The bug is assigned to somebody |
| `needs review` | The issue is under review by the maintainers |

## Documentation

The following table is a collection of functionalities that need to be implemented.

### Params

* **String** `path`: The path to the file you want.

| Function Name | Description | Input | Expected Output
| ----- | ----- | ----- | ----- |
| `getFilePathName(path)` | Filename without the path | `/home/marvins/mydata.txt` | `mydata.txt` |
| `getFileSize(path)` | File size in bytes | `/home/marvins/mydata.txt` | 129 Kb |
| `convertSHA(path)` | SHA1 digest for a file at the given path | The quick brown fox jumps over the lazy dog | 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 |
| `convertMD5(path)` | MD5 digest for a file at the given path | The quick brown fox jumps over the lazy dog | 9e107d9d372bb6826bd81d3542a419d |

#### Example

```python
# The variable path is the desired URL
path = getFilePathName('example/mydata.txt'):

# Return value on path variable is 'mydate.txt'
print path
```

## License

This project is licensed under the [MIT](docs/LICENSE.md) license.

[Marvin Sanchez](http://marvinrsanchez.wordpress.com/)
