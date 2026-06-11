import base64
import importlib
import os
import random
import string
from functools import wraps

import matplotlib.pyplot as plt
from django.db import models
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
from matplotlib.backends.backend_pdf import PdfPages
from rest_framework import serializers


class Utils:
    @staticmethod
    def get_class(config, name: str) -> models.Model:
        return Utils.model_name_to_class(config[name])

    @staticmethod
    def get_manager(config, name: str) -> models.Manager:
        return Utils.get_class(config, name).objects

    @staticmethod
    def get_serializer(config, name: str):
        class Serializer(serializers.ModelSerializer):
            class Meta:
                model = Utils.get_class(config, name)
                fields = "__all__"

        return Serializer

    @staticmethod
    def model_name_to_class(name: str):

        model_name    = name.split(".")[-1]
        model_import  = name.replace("."+model_name, "")

        module = importlib.import_module(model_import)
        return getattr(module, model_name)


def check_permission(function):
    @wraps(function)
    def wrap(viewRequest, *args, **kwargs):  # noqa: N803

        try:

            # Check user
            if viewRequest.request.user.is_authenticated:
                return function(viewRequest, *args, **kwargs)

            # All good - allow the processing
            return HttpResponseRedirect("/login/")

        except Exception as e:  # noqa: BLE001

            # On error
            return HttpResponse( "Error: " + str( e ) )

        return function(viewRequest, *args, **kwargs)

    return wrap


def get_pdf(
    data_frame,
):
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.axis("tight")
    ax.axis("off")
    ax.table(
        cellText=data_frame.values,
        colLabels=data_frame.columns,
        loc="center",
        colLoc="center",
    )
    random_file_name = get_random_string(10) + ".pdf"
    pp = PdfPages(random_file_name)
    pp.savefig(fig, bbox_inches="tight")
    pp.close()
    bytess = read_file_and_remove(random_file_name)
    return base64.b64encode(bytess).decode("utf-8")


def get_excel(
    data_frame,
):
    random_file_name = get_random_string(10) + ".xlsx"

    data_frame.to_excel(random_file_name, index=False, header=True, encoding="utf-8")
    bytess = read_file_and_remove(random_file_name)
    return base64.b64encode(bytess).decode("utf-8")


def get_csv(
    data_frame,
):
    random_file_name = get_random_string(10) + ".csv"

    data_frame.to_csv(random_file_name, index=False, header=True, encoding="utf-8")
    bytess = read_file_and_remove(random_file_name)
    return base64.b64encode(bytess).decode("utf-8")


def read_file_and_remove(path):
    with open(path, "rb") as file:  # noqa: PTH123
        bytess = file.read()
        file.close()

    # ths file pointer should be closed before removal
    os.remove(path)  # noqa: PTH107
    return bytess


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))  # noqa: S311


def _get_headings(model_class, filter_relations=True):  # noqa: FBT002
    headings = []
    for field in model_class._meta.get_fields():  # noqa: SLF001
        if filter_relations and _is_relation_field(field):
            continue
        headings.append(field.name)
    return headings


def _is_relation_field(field):
    is_many_to_many_field = field.many_to_many is not None
    is_many_to_one_field = field.many_to_one is not None
    is_one_to_many_field = field.one_to_many is not None
    is_one_to_one_field = field.one_to_one is not None
    return (
        is_many_to_many_field
        or is_many_to_one_field
        or is_one_to_many_field
        or is_one_to_one_field
    )
