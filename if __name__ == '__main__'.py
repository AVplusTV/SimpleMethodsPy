from pprint import pprint
import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {}',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def search(obj, edit, name):
    if edit in obj:
        return obj

    for k, v in obj.items():
        if isinstance(v, dict):
            res = search(v, edit, name)
            
            if res is not None:
                return res


if __name__ == '__main__':
    option = int(input('Введите кол-во сайтов:\n>>> '))
    
    for _ in range(option):
        
        sites = copy.deepcopy(site)
        name = input('\033[1;32mВведите название продукта для нового сайта:\n>>> \033[0m')
        
        for edit in ['title', 'h2']:
            res = search(sites, edit, name)
            
            for k, v in res.items():
                res[k] = res[k].format(name)
                
        sites.update(res)
        
        print('\n>>> NAME OUTPUT <<<\n')
        
        pprint(object=sites, width=72, depth=3, compact=True, sort_dicts=False)
        print()

print(__name__)