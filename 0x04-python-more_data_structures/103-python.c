#include <Python.h>
#include <bytesobject.h>
#include <stdio.h>
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_list - Prints some basic information about python list objects
 * @p: Pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}


/**
 * print_python_bytes - Prints some basic information about python byte objects
 * @p: Pointer to the Python byte object
 */
void print_python_bytes(PyObject *p)
{
	long int size, i, limit;
	char *byte_str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	byte_str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", byte_str);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (byte_str[i] >= 0)
			printf(" %02x", byte_str[i]);
		else
			printf(" %02x", 256 + byte_str[i]);

	printf("\n");
}
