#include "liborca.h"

char motif_count_func_docs[] = "Count motifs";

PyMethodDef orca_funcs[] = {
	{	"motif_counts_str",
		(PyCFunction)motif_counts_wrap,
		METH_VARARGS,
		motif_count_func_docs},
	{	NULL}
};

char orcamod_docs[] = "orca module";

PyModuleDef orca_mod = {
	PyModuleDef_HEAD_INIT,
	"orcastr",
	orcamod_docs,
	-1,
	orca_funcs,
	NULL,
	NULL,
	NULL,
	NULL
};

PyMODINIT_FUNC PyInit_orcastr(void) {
	return PyModule_Create(&orca_mod);
}
