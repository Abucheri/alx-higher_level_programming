#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Print info abt a Python list
 *
 * @p: pointer to a PyObject representing the list
 *
 * Return: Nothing
 */

void print_python_list(PyObject *p)
{
	int size, allocate, i;
	const char *t;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	allocate = list->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocate);
	for (i = 0; i < size; i++)
	{
		t = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, t);
		if (strcmp(t, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[i]);
		}
	}
}

/**
 * print_python_bytes - print info abt a Python bytes object
 *
 * @p: pointer to a PyObject representing the bytes object
 *
 * Return: Nothing
 */

void print_python_bytes(PyObject *p)
{
	unsigned char i, sz;
	PyBytesObject *b = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", b->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
	{
		sz = 10;
	}
	else
	{
		sz = ((PyVarObject *)p)->ob_size + 1;
	}
	printf("  first %d bytes: ", sz);
	for (i = 0; i < sz; i++)
	{
		printf("%02hhx", b->ob_sval[i]);
		if (i == (sz - 1))
			printf("\n");
		else
			printf(" ");
	}
}
