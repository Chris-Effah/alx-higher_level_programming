#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
	printf("[*] Python list info\n");

	if (!PyList_Check(p)) {
		printf("  [ERROR] Invalid Python list\n");
		return;
	}

HEAD
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
c39f06bd6594ba818ca3e43a3e656b82bcb72600

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++) {
HEAD
		PyObject *item = PyList_GetItem(p, i);

		PyObject *item = ((PyListObject *)p)->ob_item[i];
c39f06bd6594ba818ca3e43a3e656b82bcb72600
		const char *itemType = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, itemType);
	}
}

void print_python_bytes(PyObject *p) {
	printf("[*] Python bytes info\n");

	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Python bytes object\n");
		return;
	}

HEAD
	Py_ssize_t size = PyBytes_Size(p);
	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
c39f06bd6594ba818ca3e43a3e656b82bcb72600
	Py_ssize_t to_print = size > 10 ? 10 : size;

	printf("[*] Size of the bytes object = %ld\n", size);
	printf("first %ld bytes: ", to_print);

 HEAD
	for (Py_ssize_t i = 0; i < to_print; i++) {
		printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
	unsigned char *bytes_data = (unsigned char *)PyBytes_AsString(p);
	for (Py_ssize_t i = 0; i < to_print; i++) {
		printf("%02x", bytes_data[i]);
c39f06bd6594ba818ca3e43a3e656b82bcb72600
		if (i + 1 < to_print) {
			printf(" ");
		}
	}
	printf("\n");
}

