#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
	if (!PyList_Check(p)) {
		printf("[ERROR] Invalid PyListObject\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++) {
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p) {
	if (!PyBytes_Check(p)) {
		printf("[ERROR] Invalid PyBytesObject\n");
		return;
	}

	Py_ssize_t size = PyBytes_GET_SIZE(p);
	Py_ssize_t i;
	const char *str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes: ", size < 10 ? size : 10);
	for (i = 0; i < size && i < 10; i++) {
		printf("%02hhx", str[i]);
		if (i < size - 1 && i < 9)
			printf(" ");
	}
	printf("\n");
}

void print_python_float(PyObject *p) {
	if (!PyFloat_Check(p)) {
		printf("[ERROR] Invalid PyFloatObject\n");
		return;
	}

	printf("[.] float object info\n");

	double val = PyFloat_AS_DOUBLE(p);
	printf("  value: %g\n", val);
}

