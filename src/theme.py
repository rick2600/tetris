from constants import *
import os
import json
import glob
from pathlib import Path


class Theme:
    def __init__(self):
        self.current_idx = 0
        self.theme_names = self.get_theme_names()


    def get(self, key):
        return self.theme_map[key]


    def get_theme_names(self):
        dirname = os.path.dirname(__file__)
        path = os.path.realpath(os.path.join(dirname, '..', 'themes'))
        themes = [Path(theme).stem for theme in glob.glob(f"{path}/*.json")]
        return sorted(themes)


    def load_next(self):
        self.current_idx = (self.current_idx + 1) % len(self.theme_names)
        self.load_theme_file(self.theme_names[self.current_idx])


    def load_prev(self):
        self.current_idx -= 1
        if self.current_idx < 0:
            self.current_idx = len(self.theme_names) - 1
        self.load_theme_file(self.theme_names[self.current_idx])


    def load(self, theme_name):
        try:
            self.current_idx = self.theme_names.index(theme_name)
        except ValueError:
            pass
        self.load_theme_file(self.theme_names[self.current_idx])


    def load_theme_file(self, theme_name):
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, '..', 'themes', f'{theme_name}.json')
        os.path.realpath(path)
        theme_path = os.path.realpath(path)

        with open(theme_path) as file:
            theme = json.load(file)
            self.prepare_mapping(theme)


    def prepare_mapping(self, theme={}):
        # TODO: validate missing values and limits
        self.theme_map = {}
        self.theme_map[W] = theme.get('wall', DEFAULT_THEME['wall'])
        self.theme_map[E] = theme.get('empty', DEFAULT_THEME['empty'])
        self.theme_map[I] = theme.get('I', DEFAULT_THEME['I'])
        self.theme_map[T] = theme.get('T', DEFAULT_THEME['T'])
        self.theme_map[O] = theme.get('O', DEFAULT_THEME['O'])
        self.theme_map[Z] = theme.get('Z', DEFAULT_THEME['Z'])
        self.theme_map[S] = theme.get('S', DEFAULT_THEME['S'])
        self.theme_map[L] = theme.get('L', DEFAULT_THEME['L'])
        self.theme_map[J] = theme.get('J', DEFAULT_THEME['J'])

        bg_color = theme.get('bg-color', DEFAULT_THEME['bg-color'])
        self.theme_map['bg-color'] = bg_color

        score = theme.get('score', DEFAULT_THEME['score'])
        self.theme_map['score'] = score

        next_piece = theme.get('next-piece', DEFAULT_THEME['next-piece'])
        self.theme_map['next-piece'] = next_piece


        controls = theme.get('controls', DEFAULT_THEME['controls'])
        self.theme_map['controls'] = controls

        status = theme.get('status', DEFAULT_THEME['status'])
        self.theme_map['status'] = status
