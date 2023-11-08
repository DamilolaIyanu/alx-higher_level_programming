#include <Python.h>
/**
 *print_python_list_info - function to print python list
 *@p: pointer to the object list
 */
void print_python_list_info(PyObject *p)
{
	int size, don, a;
	PyObject *obj;

	size = Py_SIZE(p);
	don = ((PyListObject *)p)->allocated;

	printf("[*] size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", don);

	a = 0;
	while (a < size)
	{
		printf("Element %d: ", a);

		obj = PyList_GetItem(p, a);
		printf("%s\n", Py_TYPE(obj)->tp_name);
		a++;
	}
}
