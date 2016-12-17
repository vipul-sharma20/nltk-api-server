from django.http import JsonResponse


class ValidateParameterMiddleware(object):

    params = {
            'words': ['stem', 'lemma'],
            'sentence': ['tokenize', 'ner', 'tag', 'sentiment']
            }

    def process_request(self, request):
        if request.path != '/':
            segments = request.path.split('/')
            if len(segments) > 3:
                view_type = segments[2]
                message = ''
                if view_type in self.params['sentence'] and not \
                        request.GET.get('sentence'):
                    message = 'sentence'
                elif view_type in self.params['words'] and not \
                        request.GET.get('words'):
                    message = 'words'
                if message:
                    return JsonResponse({
                        'message': '%s parameter missing' % message,
                        'status': False
                    })

