#include <Python.h>
#include <stdio.h>
/**
  * print_python_list - a function that prints a python list
  * @p: python list
  * Return: Void
  */

void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid Python list\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *itemType = item->ob_type->tp_name;

		printf("Element %ld: %s\n", i, itemType);
	}
}
/**
  * print_python_bytes - a function that prints the bytes of a python list
  * @p: python list
  * Return: Void
  */

void print_python_bytes(PyObject *p)
{
	printf("[*] Python bytes info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Python bytes object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t to_print = size > 10 ? 10 : size;

	printf("[*] Size of the bytes object = %ld\n", size);
	printf("first %ld bytes: ", to_print);

	for (Py_ssize_t i = 0; i < to_print; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
		if (i + 1 < to_print)
		{
			printf(" ");
		}
	}
	printf("\n");
}

