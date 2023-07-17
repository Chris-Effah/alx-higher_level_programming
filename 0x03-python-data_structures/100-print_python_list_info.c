#include <Python.h>
/**
  * print_python_list_info - a function that prints a python list
  * @p: list to be printed
  */
void print_python_list_info(PyObject *p)
{
	Py_size_t size, i;
	PyObject *item;

	size = PyList_size(p);
	printf("[*] Size of the Python List = %d\n", size);

	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
