__author__ = "Yujie Meng"
__email__ = "mengyujiee@163.com"

from snakemake.shell import shell
reads = "{} {}".format(*snakemake.input.sample)
log = snakemake.log_fmt_shell(stdout=True, stderr=True)
database = f"--db {snakemake.params.database}"
output = f"--output {snakemake.output.outfile}"
report = f"--report {snakemake.output.report}"
classified_out = f"--classified-out {snakemake.params.classified_out_path}"
shell(
    "(kraken2"
    " --paired"
    " --gzip-compressed"
    " {classified_out}"
    " {database}"
    " {output}"
    " {report}"
    " --report-zero-counts"
    " {reads}"
") {log}"
)