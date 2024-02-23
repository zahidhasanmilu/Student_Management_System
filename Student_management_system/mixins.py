from django.shortcuts import redirect


class LogoutRequiredMixin(object):
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.user_type == '1':
                return redirect('hod_home')
            if self.request.user.user_type == '2':
                return redirect('staff_home')
            if self.request.user.user_type == '1':
                return redirect('student_home')

        return super(LogoutRequiredMixin, self).dispatch(*args, **kwargs)
