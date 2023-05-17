#include <Python.h>

/**
 * print_python_list - prints some basic info about Python lists
 * @p: PyObject
 * Return: void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: PyObject
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t i;
	char *str;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));

	if (PyBytes_AsStringAndSize(p, &str, &size) != -1)
	{
		printf("  trying string: %s\n", str);

		if (size > 10)
			size = 10;

		printf("  first %ld bytes: ", size);

		for (i = 0; i < size; i++)
		{
			printf("%02x", (unsigned char)str[i]);

			if (i < size - 1)
				printf(" ");
		}

		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
