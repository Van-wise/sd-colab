# get save_dir_id, save_dir = save_dir_id
def get_save_dir_id (save_dir):

    save_dir_id = None
    try:
        path_parts = save_dir.split('/')
        parent_id = None
        for folder_name in path_parts[4:]:
            query = f"mimeType='application/vnd.google-apps.folder' and trashed = false and name='{folder_name}'"
            if parent_id:
                query += f" and '{parent_id}' in parents"
            results = drive_service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
            folder = results.get('files', [])[0]
            save_dir_id = folder.get('id')
            parent_id = save_dir_id
    except HttpError as error:
        print(f'An error occurred: {error}')
    print(save_dir_id)
    return save_dir_id

# /models/Stable-diffusion/sdmodels
def add_shortcut_directory_to_drive (shortcut_name, share_id, save_dir_name, save_dir):

    query = f"name='{save_dir_name}' and mimeType='application/vnd.google-apps.folder' and parents in '{save_dir}'"
    results = drive_service.files().list(q=query).execute().get('files', [])
    if not results:
        raise Exception(f"No folder found with name '{save_dir_name}'.")
    
    save_dir_id = results[0]['id']
    shortcut_metadata = {
        'name': shortcut_name,
        'mimeType': 'application/vnd.google-apps.shortcut',
        'shortcutDetails': {
            'targetId': share_id
        },
        'parents': [save_dir_id]
    }
    try:
        shortcut_file = drive_service.files().create(body=shortcut_metadata, fields='id').execute()
        shortcut_id = shortcut_file['id']
        print("Shortcut created successfully!")
    
    except HttpError as error:
        print("An error occurred: %s" % error)
        shortcut_id = None
    
    return shortcut_id

# /models/Stable-diffusion/*
def add_shortcut_files_to_drive (share_id, save_dir_name, save_dir):

    query = f"name = '{save_dir_name}' and mimeType = 'application/vnd.google-apps.folder' and parents in '{save_dir}'"
    results = drive_service.files().list(q=query).execute().get('files', [])
    if not results:
        raise Exception(f"No folder found with name '{save_dir_name}'.")
    
    save_dir_id = results[0]['id']
    shortcut_id = None

    query = f"'{share_id}' in parents and mimeType != 'application/vnd.google-apps.folder'"
    results = drive_service.files().list(q=query).execute().get('files', [])
    file_ids = [result['id'] for result in results]

    for file_id in file_ids:
        file = drive_service.files().get(fileId=file_id).execute()
        file_name = file['name']
        shortcut_metadata = {
            'name': file_name,
            'mimeType': 'application/vnd.google-apps.shortcut',
            'shortcutDetails': {
               'targetId': file_id
            },
            "parents": [save_dir_id]
        }
        shortcut_file = drive_service.files().create(body=shortcut_metadata).execute()
        shortcut_id = shortcut_file['id']
        print(f"Shortcut created for {file_name} with ID: {shortcut_id}")

#delete_shortcut /models/Stable-diffusion/*
def delete_shortcut_files(save_dir):

    folder_id = get_save_dir_id(save_dir)
    
    query = f"'{folder_id}' in parents and mimeType='application/vnd.google-apps.shortcut'"
    results = drive_service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
    shortcuts = results.get('files', [])
 
    if shortcuts:
        print(f"Found {len(shortcuts)} shortcuts in folder {folder_id}:")
        for shortcut in shortcuts:
            print(f"{shortcut['name']} ({shortcut['id']})")
        for shortcut in shortcuts:
            drive_service.files().delete(fileId=shortcut['id']).execute()
        print(f"Deleted {len(shortcuts)} shortcuts")
    else:
        print(f"No shortcuts found in folder {folder_id}")