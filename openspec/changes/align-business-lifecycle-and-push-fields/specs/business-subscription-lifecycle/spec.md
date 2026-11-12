## ADDED Requirements

### Requirement: Subscription authority belongs to the current owner

The implementation SHALL bind subscription authority to the endpoint, link and accepted session context that received it. Cached application data MUST NOT grant authority to a new owner. Any early-command handoff SHALL verify the owner and preserve START/STOP order.

#### Scenario: A previous endpoint supplied START
- **WHEN** a new runtime endpoint becomes ready after a previous endpoint received START
- **THEN** the new endpoint SHALL await its own subscription unless the handoff proves that it retains the same valid owner
- **AND** global cached START fields SHALL NOT independently authorize updates

#### Scenario: STOP follows an early START
- **WHEN** the same valid owner receives START then STOP before its publisher is attached
- **THEN** attaching the publisher SHALL NOT restore the canceled subscription

### Requirement: Business revocation applies before transport commitment

The implementation SHALL revoke uncommitted business work when its subscription is stopped/replaced or its owner becomes invalid. The writer SHALL check validity before sequence allocation. Previously committed fragments SHALL retain the existing reliable-transport contract.

#### Scenario: STOP overtakes a queued update
- **WHEN** a subscribed update is queued and STOP is processed before its transport sequence is allocated
- **THEN** the update SHALL be rejected as stale without sending it or failing the replacement owner

#### Scenario: A committed frame is being fragmented
- **WHEN** an update has already crossed the transport commitment boundary before subscription revocation
- **THEN** its remaining fragments SHALL follow the established reliable-transport behavior
- **AND** newly queued updates for the revoked subscription SHALL be rejected

### Requirement: Lifecycle readiness is independently established

The implementation SHALL distinguish link suspension/resumption, platform sleep/wake and disconnection. It MUST keep business output closed while current session/feature validity is unconfirmed and SHALL preserve required link control work. An arbitrary ACK or wake notification MUST NOT itself authorize business output.

#### Scenario: Resume validity is unknown
- **WHEN** a wake/resume event arrives without confirmation of the current business/session authority
- **THEN** no subscription or business timer SHALL be automatically reactivated by that event alone
- **AND** the implementation SHALL continue the required link control and validity checks

### Requirement: Ended owners release business resources

The implementation SHALL stop new work, cancel or invalidate old callbacks, and release each ended owner's resources with repeatable cleanup. Presentation caching MAY be retained only with a documented expiry and without sending authority.

#### Scenario: An old completion arrives after reconnect
- **WHEN** owner A ends, owner B starts, and a callback belonging to A completes
- **THEN** it SHALL NOT publish into, clear, or fail B's business state

#### Scenario: Cleanup is repeated
- **WHEN** failure and explicit disconnect both request cleanup for the same owner
- **THEN** cleanup SHALL complete without duplicate resource release or restoring subscription authority
