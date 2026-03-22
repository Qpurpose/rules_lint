load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

exports_files(["ruff.toml"])

py_library(
    name = "unused_import",
    srcs = ["unused_import.py"],
)

py_library(
    name = "unsupported_operator",
    srcs = ["unsupported_operator.py"],
)

py_library(
    name = "call_non_callable",
    srcs = ["call_non_callable.py"],
)

py_library(
    name = "missing_doc_arg",
    srcs = ["missing_doc_arg.py"],
)

py_library(
    name = "uses_dependency",
    srcs = ["uses_dependency.py"],
    deps = ["//src/python_lib:py_dependency"],
)

py_library(
    name = "uses_pyi_dependency",
    srcs = ["uses_pyi_dependency.py"],
    pyi_deps = [":pyi_dependency"],
)

py_library(
    name = "missing_pyi_dependency",
    srcs = ["uses_pyi_dependency.py"],
)

py_library(
    name = "uses_eval",
    srcs = ["uses_eval.py"],
)

py_library(
    name = "uses_eval_stub",
    pyi_srcs = ["uses_eval.pyi"],
)

filegroup(
    name = "unused_import_pyi",
    srcs = ["unused_import.pyi"],
    tags = ["python"],
)

py_library(
    name = "unused_import_stub",
    pyi_srcs = ["unused_import.pyi"],
)

py_library(
    name = "pyi_dependency",
    pyi_srcs = ["//src/python_lib:dependency.pyi"],
)

filegroup(
    name = "all",
    srcs = [
        ":call_non_callable",
        ":missing_doc_arg",
        ":unsupported_operator",
        ":unused_import",
        ":uses_dependency",
        ":uses_eval",
        ":uses_pyi_dependency",
    ],
)
