from photologue.views import PhotoListView

from braces.views import JSONResponseMixin


class PhotoJSONListView(JSONResponseMixin, PhotoListView):

    def render_to_response(self, context, **response_kwargs):
        return self.render_json_object_response(context['object_list'],
                                                **response_kwargs)