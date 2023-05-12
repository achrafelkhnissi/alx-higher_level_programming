#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to PyObject
 *
 * Return: void
 */
void print_python_list_info(PyObject *p) {
  Py_ssize_t size = PyList_Size(p);
  PyObject **elements = PyList_GetItems(p);

  printf("[*] Size of the Python List = %zd\n", size);
  printf("[*] Allocated = %zd\n", PyList_GET_SIZE(p));

  for (Py_ssize_t i = 0; i < size; i++) {
    PyObject *element = elements[i];
    printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
  }

  Py_DECREF(elements);
}
