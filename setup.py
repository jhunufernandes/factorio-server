import json
import os
import pathlib
import typing

BaseDict = dict[str, typing.Any]
BaseList = list[str]
ContentType = BaseDict | BaseList

FACTORIO_DATA_PATH = pathlib.Path("./factorio/data")
NEW_CONTENT_DATA_PATH = pathlib.Path("./saves")
NEW_CONTENTS: dict[str, ContentType] = {
    "map-gen-settings": {},
    "map-settings": {},
    "server-settings": {
        "name": "Nacional-desenvolvimentismo",
        "description": "In Brizola we trust",
        "token": os.getenv("TOKEN", "") or os.getenv("token", ""),
        "game_password": "pdt",
        "visibility": {
                "public": False,
                "lan": True,
            },
    },
    "server-whitelist": [
        "jhunufernandes",
    ],
    "server-banlist": [],
    "server-adminlist": [
        "jhunufernandes",
    ]
}


def read_json_file(file_path: pathlib.Path) -> ContentType | None:
    try:
        with open(file_path, "r") as example_file:
            file_content = example_file.read()
            file_json = json.loads(file_content)
            return file_json
    except FileNotFoundError:
        return


def write_json_file(file_path: pathlib.Path, file_content: ContentType) -> None:
    with open(file_path, "w") as formated_file:
        formated_file.write(json.dumps(file_content))


def setup_files(file_name: str, new_content: ContentType) -> None:
    file_example_path = pathlib.Path(FACTORIO_DATA_PATH, f"{file_name}.example.json")
    file_example_content = read_json_file(file_example_path)
    file_path = pathlib.Path(NEW_CONTENT_DATA_PATH, f"{file_name}.json")
    file_content: ContentType = [
        *(file_example_content or []),
        *new_content,
    ] if isinstance(new_content, list) else {
        **(file_example_content or {}),  # type: ignore
        **new_content,
    }
    write_json_file(file_path, file_content)


for file_name, new_content in NEW_CONTENTS.items():
    setup_files(file_name, new_content)
