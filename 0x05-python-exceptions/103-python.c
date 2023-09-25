#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print information about a Python list object
 *
 * @p: The Python object to inspect
 *
 * Return: Nothing
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t list_size, list_alloc, index;
	const char *element_type;
	PyListObject *list_object = (PyListObject *)p;
	PyVarObject *var_object = (PyVarObject *)p;

	list_size = var_object->ob_size;
	list_alloc = list_object->allocated;
	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list_alloc);
	for (index = 0; index < list_size; index++)
	{
		element_type = list_object->ob_item[index]->ob_type->tp_name;
		printf("Element %ld: %s\n", index, element_type);
		if (strcmp(element_type, "bytes") == 0)
			print_python_bytes(list_object->ob_item[index]);
		else if (strcmp(element_type, "float") == 0)
			print_python_float(list_object->ob_item[index]);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 *
 * @p: The Python object to inspect
 *
 * Return: Nothing
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t byte_size, byte_index;
	PyBytesObject *bytes_object = (PyBytesObject *)p;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes_object->ob_sval);
	if (((PyVarObject *)p)->ob_size >= 10)
	{
		byte_size = 10;
	} else
	{
		byte_size = ((PyVarObject *)p)->ob_size + 1;
	}
	printf("  first %ld bytes: ", byte_size);
	for (byte_index = 0; byte_index < byte_size; byte_index++)
	{
		printf("%02hhx", bytes_object->ob_sval[byte_index]);
		if (byte_index == (byte_size - 1))
		{
			printf("\n");
		} else
		{
			printf(" ");
		}
	}
}

/**
 * print_python_float - Print information about a Python float object
 *
 * @p: The Python object to inspect
 *
 * Return: Nothing
 */

void print_python_float(PyObject *p)
{
	char *float_buffer = NULL;

	PyFloatObject *float_object = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	float_buffer = PyOS_double_to_string(float_object->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", float_buffer);
	PyMem_Free(float_buffer);
}
