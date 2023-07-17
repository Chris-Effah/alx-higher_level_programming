#include <Python.h>
/**
  * print_python_list_info - a function that prints a python list
  * @p: list to be printed
  */
void print_python_list_info(PyObject *p)
{
	int size, i, alloc;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", size);

	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
