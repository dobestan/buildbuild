from django import forms

class MakeProjectForm(forms.Form):
    # Make project should be implemented in team page,
    # not in form field
    # team name automatically need to be set
    projects_project_name = forms.CharField(
                                max_length = 64,
                                required = True,
                                label = "Project Name",
                                )

    language = forms.CharField(
                   max_length = 20,
                   required = False,
                   label = "Language",
               )

    version = forms.CharField(
                  max_length = 20,
                  required = False,
                  label = "Language Version",
              )

    git_url = forms.URLField(
                  required = False,
                  label = "Git Clone URL",
              )

    branch_name = forms.CharField(
                      max_length = 20,
                      required = False,
                      label = "Git Branch Name",
                  )

