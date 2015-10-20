import os, sublime_plugin
class BashCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_name=self.view.file_name()
        path=file_name.split(os.sep)
        current_driver=path[0]
        path.pop()
        current_directory=os.sep.join(path)
        command= 'cd '+current_directory+' & '+current_driver+' & bash --login -i'
        os.system(command)
 
