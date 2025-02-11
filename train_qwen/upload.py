from modelscope.hub.api import HubApi

YOUR_ACCESS_TOKEN = 'fe247063-c07a-4bd8-b4bd-39ae56967e19'
api = HubApi()
api.login(YOUR_ACCESS_TOKEN)

api.create_model(
    f"Meonex/Qwen2.5-0.5B-Instruct-16bit",
    visibility=1,
    chinese_name="Qwen2.5-0.5B-Instruct-16bit"
)

api.upload_folder(
    repo_id=f"Meonex/Qwen2.5-0.5B-Instruct-16bit",
    folder_path='./qwen2.5-export-merged_16bit',
    commit_message='upload model folder to repo',
)