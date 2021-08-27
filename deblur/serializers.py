from rest_framework import serializers

from PIL import Image as ImagePIL

import os
import subprocess

from drfx.settings import BASE_DIR, MEDIA_ROOT, MEDIA_URL
from deblur.models import DeblurData


class DeblurDataSerializer(serializers.ModelSerializer):
    # deblur_data_text = serializers.CharField()
    image = serializers.ImageField(
        max_length=None, allow_empty_file=True, required=False
    )

    class Meta:
        model = DeblurData
        fields = (
            "id",
            "image",
            "created",
            "modified",
        )

    def create(self, validated_data):
        imgpath = MEDIA_ROOT + "/uploads/" + str(validated_data["image"])
        outputimgpath = (
            "/home/admin/Public/work/csh/ai_design_apis/drfx-deblur/drfx/utils/code/output/deblur4_"
            + str(validated_data["image"])
        )

        # Saving uploaded image
        img = ImagePIL.open(validated_data["image"])
        img.save(imgpath)

        apply = ["--apply"]
        file_path = ["--file-path", imgpath]

        wpath = (
            "/home/admin/Public/work/csh/ai_design_apis/drfx-deblur/drfx/utils/code/"
        )
        os.chdir(wpath)

        subprocess.call(["python", "deblur.py"] + apply + file_path, shell=False)

        # img = ImagePIL.open(outputimgpath)
        validated_data["image"] = outputimgpath
        deblurdata = DeblurData.objects.create(**validated_data)

        return deblurdata
