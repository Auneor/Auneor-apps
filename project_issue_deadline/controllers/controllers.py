# -*- coding: utf-8 -*-
from odoo import http

# class ProjectIssueDeadline(http.Controller):
#     @http.route('/project_issue_deadline/project_issue_deadline/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_issue_deadline/project_issue_deadline/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_issue_deadline.listing', {
#             'root': '/project_issue_deadline/project_issue_deadline',
#             'objects': http.request.env['project_issue_deadline.project_issue_deadline'].search([]),
#         })

#     @http.route('/project_issue_deadline/project_issue_deadline/objects/<model("project_issue_deadline.project_issue_deadline"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_issue_deadline.object', {
#             'object': obj
#         })