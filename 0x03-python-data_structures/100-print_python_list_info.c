#include <Python.h>
/**
 *print_python_list_info - prints list info
 *
 *@p: thepointer to the list
 */
void print_python_list_info(PyObject *p)
{
	int size, i, alloc;
	PyObject *type;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		type = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(type)->tp_name);
	}
}
