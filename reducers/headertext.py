def header_text(action, head_text='Прогресс'):
    if action.action_type == 'SET_GUIDE_FILTER':
        header_texts = {'GO_BUDGET': 'Бюджет',
                        'GO_RECIPES': 'Рецепты',
                        'GO_PROGRESS': 'Прогресс',
                        'GO_LIST': 'Список',
                        'GO_GLIDER': 'Планировщик'
                        }
        return header_texts[action.guide]
    else:
        return head_text
