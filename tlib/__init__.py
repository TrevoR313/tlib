from typing import List, Dict, Callable
from sys import stdin
from os import path
from requests import get
from tqdm import tqdm
from subprocess import run
import re

<<<<<<< HEAD

def download(url: str, fname: str):
=======
def download(url: str, fname: str) -> None:
>>>>>>> c38d0a06f6e43d44d1c148338c81251dc784fdf1
    try:
        with open(fname, "ab") as f, tqdm(
        ) as bar:
            headers: Dict = {}
            pos: int = f.tell()
            if pos:
                headers["Range"] = f"bytes={pos}-"
            resp = get(url, headers=headers, stream=True)
            total_size = int(resp.headers.get("content-length", 0))
            bar.desc = fname
            bar.iterable = resp.iter_content(chunk_size=1024)
            bar.total = total_size
            bar.unit = "iB"
            bar.unit_scale = True
            bar.unit_divisor = 1024
            for data in resp.iter_content(chunk_size=1024):
                size = f.write(data)
                bar.update(size)
    except KeyboardInterrupt:
        quit()

<<<<<<< HEAD

def gen(num, sep):
    i, o = 0, ""
=======
def gen(num: int, sep: str) -> str:
    i: int = 0
    o: str = ""
>>>>>>> c38d0a06f6e43d44d1c148338c81251dc784fdf1
    while i < num:
        o += sep
        i += 1
    return o


def ezstdin():
    if stdin.isatty():
        o: bool = False
        return o
    else:
        o: List[str] = []
        for line in stdin.readlines():
            o.append(line)
        return o


def arch(line):
    e = "------------------------------------------\n|                   -`                   |\n|                  .o+`                  |\n|                 `ooo/                  |\n|                `+oooo:                 |\n|               `+oooooo:                |\n|               -+oooooo+:               |\n|             `/:-:++oooo+:              |\n|            `/++++/+++++++:             |\n|           `/++++++++++++++:            |\n|          `/+++ooooooooooooo/`          |\n|         ./ooosssso++osssssso+`         |\n|        .oossssso-````/ossssss+`        |\n|       -osssssso.      :ssssssso.       |\n|      :osssssss/        osssso+++.      |\n|     /ossssssss/        +ssssooo/-      |\n|   `/ossssso+/:-        -:/+osssso+-    |\n|  `+sso+:-`                 `.-/+oso:   |\n| `++:.                           `-/+/  |\n| .`                                 `/  |\n------------------------------------------"
    e1 = e.replace("-", "").replace("|", "")[1:]
    if line == True:
        return e
    if line == False:
        return e1


def clean(str): return str.lstrip().rstrip().strip()


def hrs(size: float, decimal_places: int=3) -> str:
    """
    Converts a file's size in bytes to a more human readable format.
    for unit in ['B','KiB','MiB','GiB','TiB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"
    """
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


def r(cmd: str) -> str: 
    return run(cmd, shell=True, capture_output=True, text=True).stdout.rstrip()


def isVideo(_file: str) -> bool:
    """
    Returns True if the file's extension matches any common video format, returns False otherwise.
    :param _file:
    :type _file: str
    :returns: A bool
    :rtype: bool
    """
    if path.splitext(_file.lower())[-1] in ['.m4v', '.mp4', '.mov', '.wmv', '.avi', '.mpg', '.mpeg', '.rmvb', '.rm', '.flv', '.asf', '.mkv', '.webm']:
        return True
    else:
        return False


def isImage(_file: str) -> bool:
    """
    Returns True if the file's extension matches any common image format, returns False otherwise.
    :param _file:
    :type _file: str
    :returns: A bool
    :rtype: bool
    """
    if path.splitext(_file.lower())[-1] in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
        return True
    else:
        return False


def isAudio(_file: str) -> bool:
    """
    Returns True if the file's extension matches any common audio format, returns False otherwise.
    :param _file:
    :type _file: str
    :returns: A bool
    :rtype: bool
    """
    if path.splitext(_file.lower())[-1] in ['.mp3', '.aac', '.ogg', '.m4a', '.wma', '.flac', '.wav']:
        return True
    else:
        return False


<<<<<<< HEAD
def parseCookieFile(cookiefile: str) -> dict:
=======
def isDir(_directory: str) -> bool:
    """
    Checks if _directory is an actual directory and returns a corresponding bool.
    :param _directory: Path the the directory.
    :type _directory: str
    :returns: A boolean that is True if _directory is a directory, returns False if it doesn't exist and/or it's not a directory.
    :rtype: bool
    """
    try:
        _dir = open(_directory, 'r')
        _dir.close()
    except IsADirectoryError:
        return True
    except FileNotFoundError:
        return False
    return False


def parseCookieFile(cookiefile: str) -> Dict[str, str]:
>>>>>>> c38d0a06f6e43d44d1c148338c81251dc784fdf1
    """Parse a cookies.txt file and return a dictionary of key value pairs
    compatible with requests."""

    cookies: Dict[str, str] = {}
    with open(cookiefile, 'r') as fp:
        for line in fp:
            if not re.match(r'^\#', line) and line not in ['\n']:
                lineFields = line.strip().split('\t')
                cookies[lineFields[-1 - 1]] = lineFields[-1]
    return cookies

<<<<<<< HEAD

def parseHeaders(Headers: str) -> dict:
=======
def parseHeaders(Headers: str) -> Dict[str, str]:
>>>>>>> c38d0a06f6e43d44d1c148338c81251dc784fdf1
    """
    Converts a multi-line string containing HTTP headers into a dictionary.
    :param Headers: A multi-line string with an HTTP header on each line.
    :type Headers: str
    :rtype: dict
    """
    parsed: Dict[str, str] = {}
    list_parsed = [
        [i.split(":")[0], i.split(":")[-1][1:]]
        if i.split(":")[-1][0] == " "
        else [i.split(":")[0], i.split(":")[-1]]
        for i in [i for i in Headers.splitlines() if i != ""]
    ]
    for i in list_parsed:
        parsed.update({i[0]: i[-1]})
    return parsed

