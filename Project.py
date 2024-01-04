{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0d639f08-1df9-42fd-a4e3-c442d8ac5523",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e43ec7c2ad70499c9652e3b3e163736b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Text(value='', description='School Code:', placeholder='Enter school code')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "28fd41e26ad647d497939ce59e49a8c4",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Suggestions:', options=('Select',), value='Select')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e3091a176a0d4636b6b64668c936bdb3",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Button(description='Search', icon='search', style=ButtonStyle(), tooltip='Click to search')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b8ee979542374cd3bed323f4426ec733",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Button(button_style='warning', description='Clear', icon='times-circle', style=ButtonStyle(), tooltip='Click t…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7b31cda00704433688b902e415b07cb9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Output()"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import ipywidgets as widgets\n",
    "from IPython.display import display\n",
    "\n",
    "# Load Excel Data\n",
    "file_path = 'your_file.xlsx'\n",
    "df = pd.read_excel(file_path)\n",
    "\n",
    "# Create Autocomplete Widget\n",
    "school_code_autocomplete = widgets.Text(\n",
    "    value='',\n",
    "    placeholder='Enter school code',\n",
    "    description='School Code:',\n",
    "    disabled=False\n",
    ")\n",
    "\n",
    "# Autocomplete Suggestions\n",
    "initial_suggestion = 'Select'\n",
    "school_code_autocomplete_suggestions = widgets.Dropdown(\n",
    "    options=[initial_suggestion],\n",
    "    value=initial_suggestion,\n",
    "    description='Suggestions:',\n",
    "    disabled=False,\n",
    ")\n",
    "\n",
    "# Create Search Button\n",
    "search_button = widgets.Button(\n",
    "    description='Search',\n",
    "    disabled=False,\n",
    "    button_style='',  # 'success', 'info', 'warning', 'danger' or ''\n",
    "    tooltip='Click to search',\n",
    "    icon='search'  # (FontAwesome names without the `fa-` prefix)\n",
    ")\n",
    "\n",
    "# Create Clear Button\n",
    "clear_button = widgets.Button(\n",
    "    description='Clear',\n",
    "    disabled=False,\n",
    "    button_style='warning',  # 'success', 'info', 'warning', 'danger' or ''\n",
    "    tooltip='Click to clear results',\n",
    "    icon='times-circle'  # (FontAwesome names without the `fa-` prefix)\n",
    ")\n",
    "\n",
    "# Display Output Result\n",
    "output_result = widgets.Output()\n",
    "\n",
    "# Define Search Function\n",
    "def search_school(b):\n",
    "    school_code = school_code_autocomplete.value\n",
    "    result = df[df['KOD SEKOLAH'] == school_code][['KOD SEKOLAH', 'SENARAI SEKOLAH MALAYSIA', 'SEKOLAH INTERIM', 'SEKOLAH VSAT', 'SEKOLAH HIBRID']]\n",
    "    \n",
    "    with output_result:\n",
    "        output_result.clear_output()\n",
    "        if result.empty:\n",
    "            print(f\"No information found for School Code: {school_code}\")\n",
    "        else:\n",
    "            # Display the output as a list\n",
    "            print(\"Information for School Code {}: \".format(school_code))\n",
    "            for _, row in result.iterrows():\n",
    "                print(\"- School Code: {}\".format(row['KOD SEKOLAH']))\n",
    "                print(\"  School Name: {}\".format(row['SENARAI SEKOLAH MALAYSIA']))\n",
    "                print(\"  TM Interim: {}\".format(row['SEKOLAH INTERIM']))\n",
    "                print(\"  VSAT: {}\".format(row['SEKOLAH VSAT']))\n",
    "                print(\"  TM Hybrid: {}\".format(row['SEKOLAH HIBRID']))\n",
    "                print(\"\\n\")\n",
    "\n",
    "# Define Clear Function\n",
    "def clear_results(b):\n",
    "    with output_result:\n",
    "        output_result.clear_output()\n",
    "    school_code_autocomplete.value = ''\n",
    "    school_code_autocomplete_suggestions.options = [initial_suggestion]\n",
    "    school_code_autocomplete_suggestions.value = initial_suggestion\n",
    "\n",
    "# Link the buttons to their respective functions\n",
    "search_button.on_click(search_school)\n",
    "clear_button.on_click(clear_results)\n",
    "\n",
    "# Function to update suggestions based on input\n",
    "def update_autocomplete_suggestions(change):\n",
    "    entered_text = change.new.upper()\n",
    "    filtered_options = [option for option in df['KOD SEKOLAH'].tolist() if option.startswith(entered_text)]\n",
    "    school_code_autocomplete_suggestions.options = [initial_suggestion] + filtered_options\n",
    "    \n",
    "# Function to update search bar based on dropdown selection\n",
    "def update_search_bar(change):\n",
    "    selected_option = change.new\n",
    "    if selected_option != 'Select':\n",
    "        school_code_autocomplete.value = selected_option\n",
    "        \n",
    "# Link the autocomplete widget to update suggestions\n",
    "school_code_autocomplete.observe(update_autocomplete_suggestions, names='value')\n",
    "\n",
    "# Link the dropdown to update search bar on selection\n",
    "school_code_autocomplete_suggestions.observe(update_search_bar, names='value')\n",
    "\n",
    "# Display widgets\n",
    "display(school_code_autocomplete, school_code_autocomplete_suggestions, search_button, clear_button)\n",
    "\n",
    "# Display the result output\n",
    "display(output_result)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31397338-e2d3-4965-afea-a495b57110a4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
