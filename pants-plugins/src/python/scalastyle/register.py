from pants.backend.jvm.tasks.scalastyle import Scalastyle
from pants.goal.task_registrar import TaskRegistrar as task


def register_goals():
  task(name='scalastyle', action=Scalastyle).install('compile')
