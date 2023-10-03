#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints Python string information.
 *
 * @p: PyObject pointer representing the string object.
 *
 * Return: Nothing
 */

void print_python_string(PyObject *p)
{
	long int str_length;

	fflush(stdout);
	printf("[.] string object info\n");
	if (strcmp(py_obj->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	str_length = ((PyASCIIObject *)(py_obj))->length;
	if (PyUnicode_IS_COMPACT_ASCII(py_obj))
	{
		printf("  type: compact ascii\n");
	} else
	{
		printf("  type: compact unicode object\n");
	}
	printf("  length: %ld\n", str_length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(py_obj, &str_length));
}
