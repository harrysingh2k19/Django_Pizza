from rest_framework  import serializers 
from .models import piza_type

class PostSerializer(serializers.ModelSerializer):
	"""docstring for PostSerializer"""
	class Meta:
		"""docstring for Meta"""
		model = piza_type
		fields = ['shape_id','size_id','choice']	