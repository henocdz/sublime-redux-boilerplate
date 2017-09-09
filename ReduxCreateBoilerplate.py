import sublime
import sublime_plugin
import os

REDUCER_CONTENT = """\
import { fromJS } from 'immutable'

export const initialState = fromJS({

})


export default function reducer(state = initialState, action) {
    switch(action.type) {
        default:
            return state
    }
}
"""

class ReduxCreateBoilerplateCommand(sublime_plugin.WindowCommand):
    """ Creates Redux Basic Boilerplate:
        - actions.js
        - reducer.js -- with reducer boilerplate using immutable.js
        - constants.js

        Inspired on SublimePythonPackage: https://github.com/curaloucura/SublimePythonPackage
    """
    def run(self, paths=None):
        paths = paths or []
        if self._is_valid_args(paths):
            self._create_files(paths[0])

    def _create_files(self, current_dir):
        for name in ['actions', 'constants']:
            file_name = '{}.js'.format(name)
            file_path = os.path.join(current_dir, file_name)
            open(file_path, 'w').close()
            self.window.open_file(file_path)

        # Create reducer.js file and append content
        reducer_path = os.path.join(current_dir, 'reducer.js')
        reducer = open(reducer_path, 'w')
        reducer.write(REDUCER_CONTENT)
        reducer.close()
        self.window.open_file(reducer_path)

    def _is_valid_args(self, paths):
        if len(paths) >= 1:
            return os.path.isdir(paths[0])
        else:
            False

    def is_enabled(self, paths = []):
        return self._is_valid_args(paths)

    def is_visible(self, paths= []):
        """ Sublime will call this method to show (or not) plugin in side bar menu
        """
        return self._is_valid_args(paths)
