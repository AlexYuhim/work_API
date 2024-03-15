import requests

# Создание вызова API в переменной
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# сохранение ответа  API в переменной
response_dict = r.json()
print(f'Total repositories: {response_dict["total_count"]}')

# Анализ информации о репозиториях
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

print('*' * 30)

# Анализ первого репозитория
# repo_dict = repo_dicts[0]
# print(f'\nKeys: {len(repo_dict)}')
# print(repo_dict)
# for key in sorted(repo_dict.keys()):
#     print(key)
for repo_dict in repo_dicts:
    print('')
    print(f'Имя : {repo_dict["name"]}')
    print(f'Владелец : {repo_dict["owner"]["login"]}')
    print(f'Звезды : {repo_dict["stargazers_count"]}')
    print(f'репо : {repo_dict["html_url"]}')
    print(f'дата создания  : {repo_dict["created_at"]}')
    print(f'дата обновления  : {repo_dict["updated_at"]}')
    print(f'описания : {repo_dict["description"]}')
    print('')
    print('*'*30)
# Обработка результатов


