from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name= serializers.CharField()
    email = serializers.EmailField()
    address =serializers.CharField(required =False)
    phone = serializers.CharField(required = False)
    age = serializers.IntegerField(required =False)
    
    
    
    def validate(self, attrs):
        name = attrs.get('name')
        email = attrs.get('email')
        # address = attrs.get('address')
        # phone = attrs.get('phone')
        # age = attrs.get('age')
        
        # errors = {}
        
        #  validate name
        # if len(name) <= 4:
            # errors['name'] = ["names must be more than 4 characters"]
            
        #  validate email
        # if not email:
            # errors['email'] = ["email is required"]
            
        # validate address
        # if not address:
            # errors['address'] = ['address is required']
        #    
        #    validate phone 
    #    if not phone:
        #    errors['phone'] = ['phone number is required']
        #    
        #    validate age 
    #    if age is None:
        #    errors['age'] = ['age is required']
        #    
    #    if errors:
        #    raise serializers.ValidationError(errors)
        
        return attrs
    
    
    def create(self, attrs):
        names = attrs.get('name')
        if len(name) <= 4:
            raise serializers.ValidationError("please name must not be less than 4 character")
        return attrs
    
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    
    def create(self, instance, validated_data):
        return super().update(instance, validated_data)
    
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance,validated_data):
        # print validated data
        print(vars(instance), "instance _dict_") 
        # only works for instance with a _dict_ attribute
        #  print (dir(instance)) list all attriibute 
        
        
        instance.name = validated_data.get("name",instance.name)
        instance.email = validated_data.get("name",instance.email)
        instance.address = validated_data.get("name",instance.address)
        instance.phone = validated_data.get("name",instance.phone)
        instance.age = validated_data.get("age",instance.age)
        instance.save()
        return instance