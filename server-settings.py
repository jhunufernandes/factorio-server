import typing
import os
import json
import pathlib


FACTORIO_DATA_PATH = pathlib.Path("../factorio/data")
BaseDict = dict[str, typing.Any]
BaseList = list[str]


def read_json_file(file_path: pathlib.Path) -> BaseDict | BaseList:
  with open(file_path, "r") as example_file:
    file_content = example_file.read()
    file_json: BaseDict = json.loads(file_content)  # type: ignore
    return file_json


map_gen_example_path = pathlib.Path(FACTORIO_DATA_PATH, "map-gen.example.json")
map_gen_example_json: BaseDict = read_json_file(map_gen_example_path)  # type: ignore
map_gen_json: BaseDict = {
  **map_gen_example_json,
}

map_settings_example_path = pathlib.Path(FACTORIO_DATA_PATH, "map-settings.example.json")
map_settings_example_json: BaseDict = read_json_file(map_settings_example_path)  # type: ignore
map_settings_json: BaseDict = {
  **map_settings_example_json,
}

server_settings_example_path = pathlib.Path(FACTORIO_DATA_PATH, "server-settings.example.json")
server_settings_example_json: BaseDict = read_json_file(server_settings_example_path)  # type: ignore
server_settings_json: BaseDict = {
  **server_settings_example_json,
  "name": "Nacional-desenvolvimentismo",
  "description": "In Brizola we trust",
  "token": os.getenv("token", ""),
  "game_password": "pdt",
}

server_whitelist_example_path = pathlib.Path(FACTORIO_DATA_PATH, "server-whitelist.example.json")
server_whitelist_example_json: BaseList = read_json_file(server_whitelist_example_path)  # type: ignore
server_whitelist_json: BaseList = [
  *server_whitelist_example_json,
]
